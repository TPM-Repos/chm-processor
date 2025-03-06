       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetRange(String,String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [XmlTemplateDocument Class](topic5909.md) > [SetRange Method](topic5926.md) : SetRange(String,String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    Name of the range to be driven.

_formula_
    Formula of the range.

_comment_
    

Glossary Item Box

Sets/adds ranges to be driven. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub SetRange( _
       ByVal _name_ As String, _
       ByVal _formula_ As String, _
       ByVal _comment_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [XmlTemplateDocument](topic5909.md)
    Dim name As String
    Dim formula As String
    Dim comment As String
     
    instance.SetRange(name, formula, comment)  
  
C#|   
---|---  
      
    
    public void SetRange( 
       string _name_ ,
       string _formula_ ,
       string _comment_
    )  
  
#### Parameters

 _name_
    Name of the range to be driven.
_formula_
    Formula of the range.
_comment_
    

# Remarks

A name must exactly equal XML file's range name.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[XmlTemplateDocument Class](topic5909.md)   
[XmlTemplateDocument Members](topic5910.md)   
[Overload List](topic5926.md)


