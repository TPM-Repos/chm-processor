Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteSpecificationMacro Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteSpecificationMacro Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macro_
    The specification macro to delete.

Glossary Item Box

Creates a transaction which when committed will delete a specification macro by name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteSpecificationMacro( _
       ByVal _macro_ As [SpecificationMacro](topic11429.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim macro As [SpecificationMacro](topic11429.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteSpecificationMacro(macro)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteSpecificationMacro( 
       [SpecificationMacro](topic11429.md) _macro_
    )  
  
#### Parameters

 _macro_
    The specification macro to delete.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


