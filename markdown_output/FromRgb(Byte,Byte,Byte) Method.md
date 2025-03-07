Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromRgb(Byte,Byte,Byte) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [SimpleColor Class](topic8856.md) > [FromRgb Method](topic8871.md) : FromRgb(Byte,Byte,Byte) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_red_
    The red component of the color.

_green_
    The green component of the color.

_blue_
    The blue component of the color.

Glossary Item Box

Initializes a new instance of the [SimpleColor](topic8856.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function FromRgb( _
       ByVal _red_ As Byte, _
       ByVal _green_ As Byte, _
       ByVal _blue_ As Byte _
    ) As [SimpleColor](topic8856.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim red As Byte
    Dim green As Byte
    Dim blue As Byte
    Dim value As [SimpleColor](topic8856.md)
     
    value = [SimpleColor](topic8856.md).FromRgb(red, green, blue)  
  
C#|   
---|---  
      
    
    public static [SimpleColor](topic8856.md) FromRgb( 
       byte _red_ ,
       byte _green_ ,
       byte _blue_
    )  
  
#### Parameters

 _red_
    The red component of the color.
_green_
    The green component of the color.
_blue_
    The blue component of the color.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SimpleColor Class](topic8856.md)   
[SimpleColor Members](topic8857.md)   
[Overload List](topic8871.md)


