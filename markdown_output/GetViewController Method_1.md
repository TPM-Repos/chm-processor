Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetViewController Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.DataTables Namespace](topic1432.md) > [IGroupDataTableDesigner Interface](topic1462.md) : GetViewController Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The running application.

_dataTable_
    The group data table to administer.

Glossary Item Box

Gets a administration controller for the given group data table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetViewController( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _dataTable_ As [GroupDataTable](topic3110.md) _
    ) As [IGroupDataTableViewController](topic1471.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupDataTableDesigner](topic1462.md)
    Dim application As [IApplication](topic24.md)
    Dim dataTable As [GroupDataTable](topic3110.md)
    Dim value As [IGroupDataTableViewController](topic1471.md)
     
    value = instance.GetViewController(application, dataTable)  
  
C#|   
---|---  
      
    
    [IGroupDataTableViewController](topic1471.md) GetViewController( 
       [IApplication](topic24.md) _application_ ,
       [GroupDataTable](topic3110.md) _dataTable_
    )  
  
#### Parameters

 _application_
    The running application.
_dataTable_
    The group data table to administer.

#### Return Value

An instance of a type which implements the [IGroupDataTableViewController](topic1471.md) interface.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupDataTableDesigner Interface](topic1462.md)   
[IGroupDataTableDesigner Members](topic1463.md)


