![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DrawingGenerationContextCreated Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IGenerationService Interface](topic15147.md) : DrawingGenerationContextCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a drawing generation context is created. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event DrawingGenerationContextCreated As EventHandler(Of DrawingGenerationContextEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IGenerationService](topic15147.md)
    Dim handler As EventHandler(Of DrawingGenerationContextEventArgs)
     
    AddHandler instance.DrawingGenerationContextCreated, handler  
  
C#|   
---|---  
      
    
    event EventHandler<DrawingGenerationContextEventArgs> DrawingGenerationContextCreated  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [DrawingGenerationContextEventArgs](topic15180.md) containing data related to this event. The following **DrawingGenerationContextEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Context](topic15187.md)| Gets the generation context.   
[IsDeferred](topic15188.md)| Gets whether the drawing being generated was deferred.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IGenerationService Interface](topic15147.md)   
[IGenerationService Members](topic15148.md)


