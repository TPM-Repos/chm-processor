Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTables Class](topic4311.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an enumerator which enumerates the data tables in the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetEnumerator() As IEnumerator(Of ProjectDataTable)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTables](topic4311.md)
    Dim value As IEnumerator(Of ProjectDataTable)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public IEnumerator<ProjectDataTable> GetEnumerator()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDataTables Class](topic4311.md)   
[ProjectDataTables Members](topic4312.md)


