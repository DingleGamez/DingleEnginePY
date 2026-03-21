#version 330 core
out vec4 FragColor;

in vec2 TexCoord;
in vec3 Normal;
in vec3 FragPos;

uniform vec3 lightPos;
uniform vec3 lightColor;
uniform sampler2D texSampler;

void main()
{
     // ambient
    float ambientStrength = 0.15;
    vec3 ambient = ambientStrength * lightColor;

    // texture
    vec4 texColor = texture(texSampler, TexCoord);
    vec3 texRGB = texture(texSampler, TexCoord).rgb;

    // diffuse
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    // specular
    float specularStrength = 1.0;
    vec3 viewDir = normalize(-FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * spec * lightColor;

    vec3 result = (ambient + diffuse + specular) * texRGB;

    FragColor = vec4(result, texColor.a);
    if(FragColor.a < 0.1)
        discard;
}