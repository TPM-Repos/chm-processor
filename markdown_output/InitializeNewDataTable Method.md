![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InitializeNewDataTable Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md) > [IDataTableDesigner Interface](topic1434.md) : InitializeNewDataTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

_creationWizard_
    The creation wizard returned by [GetCreationWizard](topic1439.md).

_dataTable_
    The data table to which to apply the settings.

Glossary Item Box

Applies the settings gathered by the creation wizard returned by [GetCreationWizard](topic1439.md) to the newly created data table. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub InitializeNewDataTable( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _creationWizard_ As [IWizard](topic613.md), _
       ByVal _dataTable_ As [ProjectDataTable](topic4282.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IDataTableDesigner](topic1434.md)
    Dim application As [IApplication](topic24.md)
    Dim creationWizard As [IWizard](topic613.md)
    Dim dataTable As [ProjectDataTable](topic4282.md)
     
    instance.InitializeNewDataTable(application, creationWizard, dataTable)  
  
C#|   
---|---  
      
    
    void InitializeNewDataTable( 
       [IApplication](topic24.md) _application_ ,
       [IWizard](topic613.md) _creationWizard_ ,
       [ProjectDataTable](topic4282.md) _dataTable_
    )  
  
#### Parameters

 _application_
    The running application.
_creationWizard_
    The creation wizard returned by [GetCreationWizard](topic1439.md).
_dataTable_
    The data table to which to apply the settings.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IDataTableDesigner Interface](topic1434.md)   
[IDataTableDesigner Members](topic1435.md)


