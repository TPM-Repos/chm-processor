![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxSetProjectMetadataSection Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13135.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxSetProjectMetadataSection( _
       ByVal _sectionName_ As String, _
       ByVal _newSectionsData_ As XElement _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Remarks

Will create the section if it does not already exist. Old data is overwritten.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
