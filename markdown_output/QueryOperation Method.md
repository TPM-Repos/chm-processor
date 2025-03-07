Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
QueryOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : QueryOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_operationName_
    The name of the operation to query.

Glossary Item Box

Queries an operation's tasks for confirmation messages that should be shown to an interactive user before invoking the operation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function QueryOperation( _
       ByVal _operationName_ As String _
    ) As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim operationName As String
    Dim value() As String
     
    value = instance.QueryOperation(operationName)  
  
C#|   
---|---  
      
    
    public string[] QueryOperation( 
       string _operationName_
    )  
  
#### Parameters

 _operationName_
    The name of the operation to query.

#### Return Value

An array of messages, e.g. "Specification x will be deleted", if no messages are collected, an empty array is returned

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


