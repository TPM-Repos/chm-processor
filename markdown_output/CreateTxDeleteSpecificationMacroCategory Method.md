Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteSpecificationMacroCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteSpecificationMacroCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macroCategory_
    The macro category to delete.

_deleteBehavior_
    The behavior to apply when deleting children.

Glossary Item Box

Creates a transaction which when committed will delete a macro category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteSpecificationMacroCategory( _
       ByVal _macroCategory_ As [SpecificationMacroCategory](topic5359.md), _
       ByVal _deleteBehavior_ As [DeleteMacroCategoryBehavior](topic2350.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim macroCategory As [SpecificationMacroCategory](topic5359.md)
    Dim deleteBehavior As [DeleteMacroCategoryBehavior](topic2350.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteSpecificationMacroCategory(macroCategory, deleteBehavior)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteSpecificationMacroCategory( 
       [SpecificationMacroCategory](topic5359.md) _macroCategory_ ,
       [DeleteMacroCategoryBehavior](topic2350.md) _deleteBehavior_
    )  
  
#### Parameters

 _macroCategory_
    The macro category to delete.
_deleteBehavior_
    The behavior to apply when deleting children.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


