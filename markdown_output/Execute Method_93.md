![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [GenerationTask Class](topic13678.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_model_
    A wrapper around the current SOLIDWORKS model.

_component_
    The current component being generated.

_generationSettings_
    The generation settings currently applied to SOLIDWORKS.

Glossary Item Box

Executes the task. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Sub Execute( _
       ByVal _model_ As SldWorksModelProxy, _
       ByVal _component_ As [ReleasedComponent](topic6324.md), _
       ByVal _generationSettings_ As [GenerationSettings](topic15238.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GenerationTask](topic13678.md)
    Dim model As SldWorksModelProxy
    Dim component As [ReleasedComponent](topic6324.md)
    Dim generationSettings As [GenerationSettings](topic15238.md)
     
    instance.Execute(model, component, generationSettings)  
  
C#|   
---|---  
      
    
    public virtual void Execute( 
       SldWorksModelProxy _model_ ,
       [ReleasedComponent](topic6324.md) _component_ ,
       [GenerationSettings](topic15238.md) _generationSettings_
    )  
  
#### Parameters

 _model_
    A wrapper around the current SOLIDWORKS model.
_component_
    The current component being generated.
_generationSettings_
    The generation settings currently applied to SOLIDWORKS.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GenerationTask Class](topic13678.md)   
[GenerationTask Members](topic13679.md)


