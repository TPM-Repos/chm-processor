![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTestController Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1454.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md) > [IDataTableTestProvider Interface](topic1449.md) : GetTestController Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

_dataTable_
    The data table for which to display data.

Glossary Item Box

Gets the controller responsible for displaying the specified data table in test mode during a specification. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetTestController( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _dataTable_ As [ProjectDataTable](topic4282.md) _
    ) As [IDataTableTestController](topic1443.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IDataTableTestProvider](topic1449.md)
    Dim application As [IApplication](topic24.md)
    Dim dataTable As [ProjectDataTable](topic4282.md)
    Dim value As [IDataTableTestController](topic1443.md)
     
    value = instance.GetTestController(application, dataTable)  
  
C#|   
---|---  
      
    
    [IDataTableTestController](topic1443.md) GetTestController( 
       [IApplication](topic24.md) _application_ ,
       [ProjectDataTable](topic4282.md) _dataTable_
    )  
  
#### Parameters

 _application_
    The running application.
_dataTable_
    The data table for which to display data.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IDataTableTestProvider Interface](topic1449.md)   
[IDataTableTestProvider Members](topic1450.md)

©2024 DriveWorks Ltd. All Rights Reserved.
