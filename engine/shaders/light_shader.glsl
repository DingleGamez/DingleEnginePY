#type vertex //THIS IS THE VERTEX SHADER
#version 330 core
layout (location = 0) in vec3 aPos;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = model * view * projection * vec4(FragPos, 1.0);
}

#type fragment //THIS IS THE FRAGMENT SHADER
#version 330 core
out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0);
}
