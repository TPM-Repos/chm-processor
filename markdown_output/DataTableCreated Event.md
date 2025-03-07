Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DataTableCreated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTables Class](topic4311.md) : DataTableCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a data table is created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event DataTableCreated As [DataTableEventHandler](topic5930.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTables](topic4311.md)
    Dim handler As [DataTableEventHandler](topic5930.md)
     
    AddHandler instance.DataTableCreated, handler  
  
C#|   
---|---  
      
    
    public event [DataTableEventHandler](topic5930.md) DataTableCreated  
  
# Event Data

The event handler receives an argument of type [DataTableEventArgs](topic2655.md) containing data related to this event. The following **DataTableEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Table](topic2665.md)| Gets the table that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDataTables Class](topic4311.md)   
[ProjectDataTables Members](topic4312.md)


