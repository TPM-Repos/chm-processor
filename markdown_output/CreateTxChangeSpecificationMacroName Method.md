Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeSpecificationMacroName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeSpecificationMacroName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macro_
    The specification macro to rename.

_newName_
    The new name to give the specification macro.

Glossary Item Box

Creates a transaction which, when committed, will rename a specification macro with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeSpecificationMacroName( _
       ByVal _macro_ As [SpecificationMacro](topic11429.md), _
       ByVal _newName_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim macro As [SpecificationMacro](topic11429.md)
    Dim newName As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeSpecificationMacroName(macro, newName)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeSpecificationMacroName( 
       [SpecificationMacro](topic11429.md) _macro_ ,
       string _newName_
    )  
  
#### Parameters

 _macro_
    The specification macro to rename.
_newName_
    The new name to give the specification macro.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


