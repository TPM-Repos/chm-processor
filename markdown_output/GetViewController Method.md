![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetViewController Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md) > [IDataTableDesigner Interface](topic1434.md) : GetViewController Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

_dataTable_
    The data table to administer.

Glossary Item Box

Gets a administration controller for the given data table. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetViewController( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _dataTable_ As [ProjectDataTable](topic4282.md) _
    ) As [IDataTableViewController](topic1455.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IDataTableDesigner](topic1434.md)
    Dim application As [IApplication](topic24.md)
    Dim dataTable As [ProjectDataTable](topic4282.md)
    Dim value As [IDataTableViewController](topic1455.md)
     
    value = instance.GetViewController(application, dataTable)  
  
C#|   
---|---  
      
    
    [IDataTableViewController](topic1455.md) GetViewController( 
       [IApplication](topic24.md) _application_ ,
       [ProjectDataTable](topic4282.md) _dataTable_
    )  
  
#### Parameters

 _application_
    The running application.
_dataTable_
    The data table to administer.

#### Return Value

An instance of a type which implements the [IDataTableViewController](topic1455.md) interface.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IDataTableDesigner Interface](topic1434.md)   
[IDataTableDesigner Members](topic1435.md)


