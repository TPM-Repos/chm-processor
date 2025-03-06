![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEditWizard Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1468.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetEditWizard( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _dataTable_ As [GroupDataTable](topic3110.md) _
    ) As [IWizard](topic613.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IGroupDataTableDesigner Interface](topic1462.md)   
[IGroupDataTableDesigner Members](topic1463.md)

©2024 DriveWorks Ltd. All Rights Reserved.
