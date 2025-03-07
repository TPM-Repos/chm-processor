Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromColor Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [SimpleColor Class](topic8856.md) : FromColor Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_color_
    The GDI color on which to base the simple color.

Glossary Item Box

Initializes a new instance of the [SimpleColor](topic8856.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromColor( _
       ByVal _color_ As Color _
    ) As [SimpleColor](topic8856.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SimpleColor Class](topic8856.md)   
[SimpleColor Members](topic8857.md)


