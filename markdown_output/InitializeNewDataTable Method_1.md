![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InitializeNewDataTable Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md) > [IGroupDataTableDesigner Interface](topic1462.md) : InitializeNewDataTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

_creationWizard_
    The creation wizard returned by [GetCreationWizard](topic1467.md).

_dataTable_
    The data table to which to apply the settings.

Glossary Item Box

Applies the settings gathered by the creation wizard returned by [GetCreationWizard](topic1467.md) to the newly created data table. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub InitializeNewDataTable( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _creationWizard_ As [IWizard](topic613.md), _
       ByVal _dataTable_ As [GroupDataTable](topic3110.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IGroupDataTableDesigner](topic1462.md)
    Dim application As [IApplication](topic24.md)
    Dim creationWizard As [IWizard](topic613.md)
    Dim dataTable As [GroupDataTable](topic3110.md)
     
    instance.InitializeNewDataTable(application, creationWizard, dataTable)  
  
C#|   
---|---  
      
    
    void InitializeNewDataTable( 
       [IApplication](topic24.md) _application_ ,
       [IWizard](topic613.md) _creationWizard_ ,
       [GroupDataTable](topic3110.md) _dataTable_
    )  
  
#### Parameters

 _application_
    The running application.
_creationWizard_
    The creation wizard returned by [GetCreationWizard](topic1467.md).
_dataTable_
    The data table to which to apply the settings.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IGroupDataTableDesigner Interface](topic1462.md)   
[IGroupDataTableDesigner Members](topic1463.md)


