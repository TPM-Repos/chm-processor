Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [TxBase Class](topic13182.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Commits the transaction. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Execute() As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TxBase](topic13182.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.Execute()  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) Execute()  
  
#### Return Value

A transaction which can undo the result of the executed transaction.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TxBase Class](topic13182.md)   
[TxBase Members](topic13183.md)


