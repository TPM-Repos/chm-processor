Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxResetSpecificationFlow Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxResetSpecificationFlow Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Creates a transaction which, when commited, will Reset the current specification to default status. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxResetSpecificationFlow() As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxResetSpecificationFlow()  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxResetSpecificationFlow()  
  
# Remarks

The inverse transaction of this is to customize the specification definition and delete all states, ready for returning back to a previous flow.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


