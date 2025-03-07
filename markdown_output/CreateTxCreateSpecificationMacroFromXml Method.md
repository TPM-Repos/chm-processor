Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateSpecificationMacroFromXml Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateSpecificationMacroFromXml Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macroXml_
    The Xml string containing the specification macro.

Glossary Item Box

Creates a transaction which, when committed, will create a specification macro from data already retrieved from the clipboard. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateSpecificationMacroFromXml( _
       ByVal _macroXml_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim macroXml As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateSpecificationMacroFromXml(macroXml)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateSpecificationMacroFromXml( 
       string _macroXml_
    )  
  
#### Parameters

 _macroXml_
    The Xml string containing the specification macro.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


