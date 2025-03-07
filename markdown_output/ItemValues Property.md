Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ItemValues Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectListItemData Class](topic4555.md) : ItemValues Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The values from the item. Key is column name and value is the current value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property ItemValues As Dictionary(Of String,String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectListItemData](topic4555.md)
    Dim value As Dictionary(Of String,String)
     
    value = instance.ItemValues  
  
C#|   
---|---  
      
    
    public Dictionary<string,string> ItemValues {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectListItemData Class](topic4555.md)   
[ProjectListItemData Members](topic4556.md)


