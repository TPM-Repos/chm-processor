Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFoldersRule Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecialVariables Class](topic4782.md) : AdditionalFoldersRule Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the rule used to determine the list of additional folders. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Property AdditionalFoldersRule As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecialVariables](topic4782.md)
    Dim value As String
     
    instance.AdditionalFoldersRule = value
     
    value = instance.AdditionalFoldersRule  
  
C#|   
---|---  
      
    
    public abstract string AdditionalFoldersRule {get; set;}  
  
# Remarks

Each individual additional folder should be delimited by a pipe-bar character, e.g. the rule `="Folder 1|Folder 2|Folder 2\Folder 3"` would create 3 folders, Folder 1, Folder 2, and Folder 3 inside Folder 2. If absolute path information is not specified, additional folders are created relative to the default specification directory.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecialVariables Class](topic4782.md)   
[ProjectSpecialVariables Members](topic4783.md)


