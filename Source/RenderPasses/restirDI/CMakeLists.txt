add_plugin(restirDI)

target_sources(restirDI PRIVATE
    restirDI.cpp
    restirDI.h
    restirDI.rt.slang
)

target_copy_shaders(restirDI RenderPasses/restirDI)

target_source_group(restirDI "RenderPasses")
