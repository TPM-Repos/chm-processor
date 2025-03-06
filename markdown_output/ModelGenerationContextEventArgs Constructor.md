![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ModelGenerationContextEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15270.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [ModelGenerationContextEventArgs Class](topic15264.md) : ModelGenerationContextEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The generation context.

Glossary Item Box

Initializes a new instance of the [ModelGenerationContextEventArgs](topic15264.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _context_ As [IModelGenerationContext](topic15157.md) _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim context As [IModelGenerationContext](topic15157.md)
     
    Dim instance As New [ModelGenerationContextEventArgs](topic15264.md)(context)  
  
C#|   
---|---  
      
    
    public ModelGenerationContextEventArgs( 
       [IModelGenerationContext](topic15157.md) _context_
    )  
  
#### Parameters

 _context_
    The generation context.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ModelGenerationContextEventArgs Class](topic15264.md)   
[ModelGenerationContextEventArgs Members](topic15265.md)

©2024 DriveWorks Ltd. All Rights Reserved.
