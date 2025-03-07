Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : GetData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets information about the child specifications that have been added to the current project or specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetData() As DataTable  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim value As DataTable
     
    value = instance.GetData()  
  
C#|   
---|---  
      
    
    public DataTable GetData()  
  
#### Return Value

An instance of the System.Data.DataTable type which has been populated with information about the child specifications. The data table consists of one row for each specification, and is populated with the data for each column in the [VariableColumns](topic4043.md) property, as well as two additional columns called Name and Type which identify the child specification name, and the project from which the specification was created.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)


