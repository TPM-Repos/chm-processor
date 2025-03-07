Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExecuteCore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TxBase Class](topic13182.md) : ExecuteCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

When overridden by a derived class, commits the transaction. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Function ExecuteCore() As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TxBase](topic13182.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.ExecuteCore()  
  
C#|   
---|---  
      
    
    protected abstract [ITransaction](topic12837.md) ExecuteCore()  
  
#### Return Value

A transaction which can undo the result of the executed transaction.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TxBase Class](topic13182.md)   
[TxBase Members](topic13183.md)


