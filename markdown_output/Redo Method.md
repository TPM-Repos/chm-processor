Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Redo Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ITransactionManager Interface](topic502.md) : Redo Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Redoes the last transaction in the redo chain. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function Redo() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ITransactionManager](topic502.md)
    Dim value As Boolean
     
    value = instance.Redo()  
  
C#|   
---|---  
      
    
    bool Redo()  
  
#### Return Value

True if there was a transaction in the redo chain, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ITransactionManager Interface](topic502.md)   
[ITransactionManager Members](topic503.md)


