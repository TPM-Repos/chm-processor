![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnAdditionalFileGenerated Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileFormatGenerator Class](topic13579.md) : OnAdditionalFileGenerated Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_args_
    The data for the event.

Glossary Item Box

Raises the [AdditionalFileGenerated](topic13606.md) event. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnAdditionalFileGenerated( _
       ByVal _args_ As [FileFormatGenerationEventArgs](topic15202.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FileFormatGenerator](topic13579.md)
    Dim args As [FileFormatGenerationEventArgs](topic15202.md)
     
    instance.OnAdditionalFileGenerated(args)  
  
C#|   
---|---  
      
    
    protected virtual void OnAdditionalFileGenerated( 
       [FileFormatGenerationEventArgs](topic15202.md) _args_
    )  
  
#### Parameters

 _args_
    The data for the event.

# ![](dotnetimages/collapse.gif)Remarks

Should only be used for additional files (besides the main additional files).

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FileFormatGenerator Class](topic13579.md)   
[FileFormatGenerator Members](topic13580.md)


