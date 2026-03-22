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
    float ambientStrength = 0.0;
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
    vec3 viewDir = normalize(-FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = 0.0;
    vec3 halfwayDir = normalize(lightDir + viewDir);
    spec = pow(max(dot(norm, halfwayDir), 0.0), 32.0);
    vec3 specular = spec * lightColor;

    // simple attenuation
    bool gamma = true;

    float max_distance = 1.5;
    float distance = length(lightPos - FragPos);
    float attenuation = 1.0 / (gamma ? distance * distance : distance);

    diffuse *= attenuation;
    specular *= attenuation;

    texRGB *= (diffuse + specular + ambient);
    if (gamma) {
        texRGB = pow(texRGB, vec3(1.0/2.2));
    }

    FragColor = vec4(texRGB, texColor.a);
    if(FragColor.a < 0.1)
        discard;
}