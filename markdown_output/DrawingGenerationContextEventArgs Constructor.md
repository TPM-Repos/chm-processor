![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DrawingGenerationContextEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15186.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [DrawingGenerationContextEventArgs Class](topic15180.md) : DrawingGenerationContextEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The generation context.

_isDeferred_
    Whether the drawing being generated was deferred.

Glossary Item Box

Initializes a new instance of the [DrawingGenerationContextEventArgs](topic15180.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _context_ As [IDrawingGenerationContext](topic15135.md), _
       ByVal _isDeferred_ As Boolean _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim context As [IDrawingGenerationContext](topic15135.md)
    Dim isDeferred As Boolean
     
    Dim instance As New [DrawingGenerationContextEventArgs](topic15180.md)(context, isDeferred)  
  
C#|   
---|---  
      
    
    public DrawingGenerationContextEventArgs( 
       [IDrawingGenerationContext](topic15135.md) _context_ ,
       bool _isDeferred_
    )  
  
#### Parameters

 _context_
    The generation context.
_isDeferred_
    Whether the drawing being generated was deferred.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DrawingGenerationContextEventArgs Class](topic15180.md)   
[DrawingGenerationContextEventArgs Members](topic15181.md)

©2024 DriveWorks Ltd. All Rights Reserved.
