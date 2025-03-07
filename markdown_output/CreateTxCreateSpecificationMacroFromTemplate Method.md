Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateSpecificationMacroFromTemplate Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateSpecificationMacroFromTemplate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the specification macro to be created.

_category_
    The category that the specification macro will belong to.

_macroXml_
    The XML containing the specification macro.

Glossary Item Box

Creates a transaction which, when comitted, will create a specification macro from an XML template. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateSpecificationMacroFromTemplate( _
       ByVal _name_ As String, _
       ByVal _category_ As String, _
       ByVal _macroXml_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim name As String
    Dim category As String
    Dim macroXml As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateSpecificationMacroFromTemplate(name, category, macroXml)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateSpecificationMacroFromTemplate( 
       string _name_ ,
       string _category_ ,
       string _macroXml_
    )  
  
#### Parameters

 _name_
    The name of the specification macro to be created.
_category_
    The category that the specification macro will belong to.
_macroXml_
    The XML containing the specification macro.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


