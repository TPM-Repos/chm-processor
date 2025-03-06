![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCreationWizard Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1439.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md) > [IDataTableDesigner Interface](topic1434.md) : GetCreationWizard Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

Glossary Item Box

Gets a wizard used to configure a new data table of the supported type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetCreationWizard( _
       ByVal _application_ As [IApplication](topic24.md) _
    ) As [IWizard](topic613.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IDataTableDesigner](topic1434.md)
    Dim application As [IApplication](topic24.md)
    Dim value As [IWizard](topic613.md)
     
    value = instance.GetCreationWizard(application)  
  
C#|   
---|---  
      
    
    [IWizard](topic613.md) GetCreationWizard( 
       [IApplication](topic24.md) _application_
    )  
  
#### Parameters

 _application_
    The running application.

# ![](dotnetimages/collapse.gif)Remarks

The wizard must not actually create the data table, it can only gather information from the user which will be used to create the data table.

The data table will be created by the application, and passed along with the wizard to the [InitializeNewDataTable](topic1442.md) method as soon as the wizard completes.

If a null reference (Nothing in Visual Basic) is returned, then no further wizard will be shown but the [InitializeNewDataTable](topic1442.md) method will still be called in case the designer needs to perform any basic initialization.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IDataTableDesigner Interface](topic1434.md)   
[IDataTableDesigner Members](topic1435.md)

©2024 DriveWorks Ltd. All Rights Reserved.
