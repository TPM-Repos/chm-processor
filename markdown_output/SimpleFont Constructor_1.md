       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SimpleFont Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [SimpleFont Class](topic8882.md) : SimpleFont Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_family_
    The family name of the font.

_size_
    The size of the font in points.

_isBold_
    Whether the font is displayed in bold face.

_isItalic_
    Whether the font is displayed in italics.

_hasUnderline_
    Whether the font has an underline.

_hasStrikethrough_
    Whether the font has a strikethrough.

Glossary Item Box

Initializes a new instance of the [SimpleFont](topic8882.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _family_ As String, _
       ByVal _size_ As Double, _
       ByVal _isBold_ As Boolean, _
       ByVal _isItalic_ As Boolean, _
       ByVal _hasUnderline_ As Boolean, _
       ByVal _hasStrikethrough_ As Boolean _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim family As String
    Dim size As Double
    Dim isBold As Boolean
    Dim isItalic As Boolean
    Dim hasUnderline As Boolean
    Dim hasStrikethrough As Boolean
     
    Dim instance As New [SimpleFont](topic8882.md)(family, size, isBold, isItalic, hasUnderline, hasStrikethrough)  
  
C#|   
---|---  
      
    
    public SimpleFont( 
       string _family_ ,
       double _size_ ,
       bool _isBold_ ,
       bool _isItalic_ ,
       bool _hasUnderline_ ,
       bool _hasStrikethrough_
    )  
  
#### Parameters

 _family_
    The family name of the font.
_size_
    The size of the font in points.
_isBold_
    Whether the font is displayed in bold face.
_isItalic_
    Whether the font is displayed in italics.
_hasUnderline_
    Whether the font has an underline.
_hasStrikethrough_
    Whether the font has a strikethrough.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SimpleFont Class](topic8882.md)   
[SimpleFont Members](topic8883.md)


