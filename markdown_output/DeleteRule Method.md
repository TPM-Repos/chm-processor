Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeleteRule Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IDataExportDefinition Interface](topic2177.md) : DeleteRule Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rule_
    The rule to be deleted.

Glossary Item Box

Deletes the specified rule from the data export document. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub DeleteRule( _
       ByVal _rule_ As [ProjectDocumentRule](topic4399.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IDataExportDefinition](topic2177.md)
    Dim rule As [ProjectDocumentRule](topic4399.md)
     
    instance.DeleteRule(rule)  
  
C#|   
---|---  
      
    
    void DeleteRule( 
       [ProjectDocumentRule](topic4399.md) _rule_
    )  
  
#### Parameters

 _rule_
    The rule to be deleted.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IDataExportDefinition Interface](topic2177.md)   
[IDataExportDefinition Members](topic2178.md)


