from falcor import *

def render_graph_restirDI():
    g = RenderGraph("restirDI")
    AccumulatePass = createPass("AccumulatePass", {'enabled': False, 'precisionMode': 'Single'})
    g.addPass(AccumulatePass, "AccumulatePass")
    ToneMapper = createPass("ToneMapper", {'autoExposure': False, 'exposureCompensation': 0.0})
    g.addPass(ToneMapper, "ToneMapper")
    restirDI = createPass("restirDI", {'maxBounces': 0})
    g.addPass(restirDI, "restirDI")
    VBufferRT = createPass("VBufferRT", {'samplePattern': 'Stratified', 'sampleCount': 16})
    g.addPass(VBufferRT, "VBufferRT")
    g.addEdge("AccumulatePass.output", "ToneMapper.src")
    g.addEdge("VBufferRT.vbuffer", "restirDI.vbuffer")
    g.addEdge("VBufferRT.viewW", "restirDI.viewW")
    g.addEdge("restirDI.color", "AccumulatePass.input")
    g.markOutput("ToneMapper.dst")
    return g

restirDI = render_graph_restirDI()
try: m.addGraph(restirDI)
except NameError: None
