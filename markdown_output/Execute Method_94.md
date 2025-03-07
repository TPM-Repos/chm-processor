Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation.Extensibility.GenerationTasks.Tasks Namespace](topic15301.md) > [DeleteFeatureGenerationTask Class](topic15309.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_model_
    

_component_
    

_generationSettings_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Sub Execute( _
       ByVal _model_ As SldWorksModelProxy, _
       ByVal _component_ As [ReleasedComponent](topic6324.md), _
       ByVal _generationSettings_ As [GenerationSettings](topic15238.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DeleteFeatureGenerationTask](topic15309.md)
    Dim model As SldWorksModelProxy
    Dim component As [ReleasedComponent](topic6324.md)
    Dim generationSettings As [GenerationSettings](topic15238.md)
     
    instance.Execute(model, component, generationSettings)  
  
C#|   
---|---  
      
    
    public override void Execute( 
       SldWorksModelProxy _model_ ,
       [ReleasedComponent](topic6324.md) _component_ ,
       [GenerationSettings](topic15238.md) _generationSettings_
    )  
  
#### Parameters

 _model_
    
_component_
    
_generationSettings_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DeleteFeatureGenerationTask Class](topic15309.md)   
[DeleteFeatureGenerationTask Members](topic15310.md)


