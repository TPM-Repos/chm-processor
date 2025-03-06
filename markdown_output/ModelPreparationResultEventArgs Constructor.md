![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ModelPreparationResultEventArgs Constructor   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [ModelPreparationResultEventArgs Class](topic15272.md) : ModelPreparationResultEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_result_
    The result of preparing the model.

_previouslyFailed_
    True if, while preparing the model, it was determined that an attempt to generate the model on a previous occasion had failed.

Glossary Item Box

Initializes a new instance of the [ModelPreparationResultEventArgs](topic15272.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _result_ As [ModelPreparationResult](topic15169.md), _
       ByVal _previouslyFailed_ As Boolean _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim result As [ModelPreparationResult](topic15169.md)
    Dim previouslyFailed As Boolean
     
    Dim instance As New [ModelPreparationResultEventArgs](topic15272.md)(result, previouslyFailed)  
  
C#|   
---|---  
      
    
    public ModelPreparationResultEventArgs( 
       [ModelPreparationResult](topic15169.md) _result_ ,
       bool _previouslyFailed_
    )  
  
#### Parameters

 _result_
    The result of preparing the model.
_previouslyFailed_
    True if, while preparing the model, it was determined that an attempt to generate the model on a previous occasion had failed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ModelPreparationResultEventArgs Class](topic15272.md)   
[ModelPreparationResultEventArgs Members](topic15273.md)


