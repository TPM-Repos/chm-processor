Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListDef Class](topic4511.md) : GetData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets information about the item that have been added to the current project or specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetData() As DataTable  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListDef](topic4511.md)
    Dim value As DataTable
     
    value = instance.GetData()  
  
C#|   
---|---  
      
    
    public DataTable GetData()  
  
#### Return Value

An instance of the System.Data.DataTable type which has been populated with information about the item. The data table consists of one row for each item, and is populated with the data for each column in the [Columns](topic4527.md) property, as well as two additional columns called Name and Type which identify the item name, and the dialog from which the item was created.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)


