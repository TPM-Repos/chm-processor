Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTransactionFactory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : CreateTransactionFactory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Creates a transaction factory which can be used to create transactions for common project modification operations. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTransactionFactory() As [ProjectTransactionFactory](topic12928.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim value As [ProjectTransactionFactory](topic12928.md)
     
    value = instance.CreateTransactionFactory()  
  
C#|   
---|---  
      
    
    public [ProjectTransactionFactory](topic12928.md) CreateTransactionFactory()  
  
#### Return Value

An instance of the [DriveWorks.Transactions.ProjectTransactionFactory](topic12928.md) class.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


