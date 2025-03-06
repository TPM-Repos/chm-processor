![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromArgb Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [SimpleColor Class](topic8856.md) : FromArgb Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_alpha_
    The alpha component of the color.

_red_
    The red component of the color.

_green_
    The green component of the color.

_blue_
    The blue component of the color.

Glossary Item Box

Initializes a new instance of the [SimpleColor](topic8856.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromArgb( _
       ByVal _alpha_ As Byte, _
       ByVal _red_ As Byte, _
       ByVal _green_ As Byte, _
       ByVal _blue_ As Byte _
    ) As [SimpleColor](topic8856.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim alpha As Byte
    Dim red As Byte
    Dim green As Byte
    Dim blue As Byte
    Dim value As [SimpleColor](topic8856.md)
     
    value = [SimpleColor](topic8856.md).FromArgb(alpha, red, green, blue)  
  
C#|   
---|---  
      
    
    public static [SimpleColor](topic8856.md) FromArgb( 
       byte _alpha_ ,
       byte _red_ ,
       byte _green_ ,
       byte _blue_
    )  
  
#### Parameters

 _alpha_
    The alpha component of the color.
_red_
    The red component of the color.
_green_
    The green component of the color.
_blue_
    The blue component of the color.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SimpleColor Class](topic8856.md)   
[SimpleColor Members](topic8857.md)


