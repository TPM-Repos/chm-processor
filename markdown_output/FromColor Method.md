![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromColor Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic8869.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [SimpleColor Class](topic8856.md) : FromColor Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_color_
    The GDI color on which to base the simple color.

Glossary Item Box

Initializes a new instance of the [SimpleColor](topic8856.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromColor( _
       ByVal _color_ As Color _
    ) As [SimpleColor](topic8856.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim color As Color
    Dim value As [SimpleColor](topic8856.md)
     
    value = [SimpleColor](topic8856.md).FromColor(color)  
  
C#|   
---|---  
      
    
    public static [SimpleColor](topic8856.md) FromColor( 
       Color _color_
    )  
  
#### Parameters

 _color_
    The GDI color on which to base the simple color.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SimpleColor Class](topic8856.md)   
[SimpleColor Members](topic8857.md)

©2024 DriveWorks Ltd. All Rights Reserved.
