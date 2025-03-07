Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRange Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [WordDocument Class](topic5885.md) : GetRange Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    Name of the driven range.

Glossary Item Box

Get the rule for a driven bookmark. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetRange( _
       ByVal _name_ As String _
    ) As [ProjectDocumentRule](topic4399.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WordDocument](topic5885.md)
    Dim name As String
    Dim value As [ProjectDocumentRule](topic4399.md)
     
    value = instance.GetRange(name)  
  
C#|   
---|---  
      
    
    public [ProjectDocumentRule](topic4399.md) GetRange( 
       string _name_
    )  
  
#### Parameters

 _name_
    Name of the driven range.

#### Return Value

The formula for the driven range, or nothing if it does not exist.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WordDocument Class](topic5885.md)   
[WordDocument Members](topic5886.md)


