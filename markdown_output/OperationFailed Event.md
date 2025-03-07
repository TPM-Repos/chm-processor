Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OperationFailed Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISpecificationRequestWithEdit Interface](topic478.md) : OperationFailed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when the specification is being edited and a operation with the given name is invalid. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event OperationFailed As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationRequestWithEdit](topic478.md)
    Dim handler As EventHandler
     
    AddHandler instance.OperationFailed, handler  
  
C#|   
---|---  
      
    
    event EventHandler OperationFailed  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationRequestWithEdit Interface](topic478.md)   
[ISpecificationRequestWithEdit Members](topic479.md)


