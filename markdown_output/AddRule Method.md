Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IDataExportDefinition Interface](topic2177.md) : AddRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The id for the new rule.

_formula_
    The rule to set.

Glossary Item Box

Adds the specified rule to the data export document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function AddRule( _
       ByVal _id_ As String, _
       ByVal _formula_ As String _
    ) As [ProjectDocumentRule](topic4399.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDataExportDefinition](topic2177.md)
    Dim id As String
    Dim formula As String
    Dim value As [ProjectDocumentRule](topic4399.md)
     
    value = instance.AddRule(id, formula)  
  
C#|   
---|---  
      
    
    [ProjectDocumentRule](topic4399.md) AddRule( 
       string _id_ ,
       string _formula_
    )  
  
#### Parameters

 _id_
    The id for the new rule.
_formula_
    The rule to set.

#### Return Value

The newly added rule.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDataExportDefinition Interface](topic2177.md)   
[IDataExportDefinition Members](topic2178.md)


