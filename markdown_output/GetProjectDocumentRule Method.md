Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetProjectDocumentRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [AdvancedXmlDocument Class](topic2364.md) : GetProjectDocumentRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The Id of the required rule.

Glossary Item Box

Gets the [ProjectDocumentRule](topic4399.md) associated with this Id. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetProjectDocumentRule( _
       ByVal _id_ As String _
    ) As [ProjectDocumentRule](topic4399.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [AdvancedXmlDocument](topic2364.md)
    Dim id As String
    Dim value As [ProjectDocumentRule](topic4399.md)
     
    value = instance.GetProjectDocumentRule(id)  
  
C#|   
---|---  
      
    
    public [ProjectDocumentRule](topic4399.md) GetProjectDocumentRule( 
       string _id_
    )  
  
#### Parameters

 _id_
    The Id of the required rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AdvancedXmlDocument Class](topic2364.md)   
[AdvancedXmlDocument Members](topic2365.md)


