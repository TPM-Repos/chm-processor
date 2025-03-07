Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEditWizard Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md) > [IGroupDataTableDesigner Interface](topic1462.md) : GetEditWizard Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

_dataTable_
    The group data table to edit.

Glossary Item Box

Gets a wizard used to configure a group data table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetEditWizard( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _dataTable_ As [GroupDataTable](topic3110.md) _
    ) As [IWizard](topic613.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupDataTableDesigner](topic1462.md)
    Dim application As [IApplication](topic24.md)
    Dim dataTable As [GroupDataTable](topic3110.md)
    Dim value As [IWizard](topic613.md)
     
    value = instance.GetEditWizard(application, dataTable)  
  
C#|   
---|---  
      
    
    [IWizard](topic613.md) GetEditWizard( 
       [IApplication](topic24.md) _application_ ,
       [GroupDataTable](topic3110.md) _dataTable_
    )  
  
#### Parameters

 _application_
    The running application.
_dataTable_
    The group data table to edit.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupDataTableDesigner Interface](topic1462.md)   
[IGroupDataTableDesigner Members](topic1463.md)


