Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxSetProjectMetadataSection Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxSetProjectMetadataSection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sectionName_
    The name of the section to update.

_newSectionsData_
    The new data to place in the section.

Glossary Item Box

Creates a transaction that will set the data element for a project metadata section. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxSetProjectMetadataSection( _
       ByVal _sectionName_ As String, _
       ByVal _newSectionsData_ As XElement _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim sectionName As String
    Dim newSectionsData As XElement
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxSetProjectMetadataSection(sectionName, newSectionsData)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxSetProjectMetadataSection( 
       string _sectionName_ ,
       XElement _newSectionsData_
    )  
  
#### Parameters

 _sectionName_
    The name of the section to update.
_newSectionsData_
    The new data to place in the section.

# Remarks

Will create the section if it does not already exist. Old data is overwritten.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


