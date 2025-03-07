Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromRgb(Int32) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [SimpleColor Class](topic8856.md) > [FromRgb Method](topic8871.md) : FromRgb(Int32) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rgb_
    An integer containing the red, green, and blue color information.

Glossary Item Box

Initializes a new instance of the [SimpleColor](topic8856.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function FromRgb( _
       ByVal _rgb_ As Integer _
    ) As [SimpleColor](topic8856.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim rgb As Integer
    Dim value As [SimpleColor](topic8856.md)
     
    value = [SimpleColor](topic8856.md).FromRgb(rgb)  
  
C#|   
---|---  
      
    
    public static [SimpleColor](topic8856.md) FromRgb( 
       int _rgb_
    )  
  
#### Parameters

 _rgb_
    An integer containing the red, green, and blue color information.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SimpleColor Class](topic8856.md)   
[SimpleColor Members](topic8857.md)   
[Overload List](topic8871.md)


