#version 460

layout (location = 0) in vec3 in_position;
layout (location = 1) in vec3 in_normal;

out Attributes {
	vec3 fragPosition;
	vec3 normal;
} outAttributes;

uniform	mat4 model;
uniform	mat4 view;
uniform	mat4 projection;

void main() 
{
	outAttributes.fragPosition = vec3(model * vec4(in_position, 1.f));
	outAttributes.normal = normalize(mat3(transpose(inverse(model))) * in_normal);
	gl_Position = projection * view * vec4(outAttributes.fragPosition, 1.f);
}