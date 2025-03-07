Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeSpecificationMacroConsistencyLevel Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeSpecificationMacroConsistencyLevel Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macro_
    The specification macro to update.

_newConsistencyLevel_
    The new consistencyLevel.

Glossary Item Box

Creates a transaction which when committed will change the specified macro's consistency level. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeSpecificationMacroConsistencyLevel( _
       ByVal _macro_ As [SpecificationMacro](topic11429.md), _
       ByVal _newConsistencyLevel_ As [MacroConsistencyLevel](topic10769.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim macro As [SpecificationMacro](topic11429.md)
    Dim newConsistencyLevel As [MacroConsistencyLevel](topic10769.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeSpecificationMacroConsistencyLevel(macro, newConsistencyLevel)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeSpecificationMacroConsistencyLevel( 
       [SpecificationMacro](topic11429.md) _macro_ ,
       [MacroConsistencyLevel](topic10769.md) _newConsistencyLevel_
    )  
  
#### Parameters

 _macro_
    The specification macro to update.
_newConsistencyLevel_
    The new consistencyLevel.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


