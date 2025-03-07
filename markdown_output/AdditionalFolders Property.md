Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFolders Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecialVariables Class](topic4782.md) : AdditionalFolders Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the calculated list of additional folders to create. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride ReadOnly Property AdditionalFolders As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecialVariables](topic4782.md)
    Dim value() As String
     
    value = instance.AdditionalFolders  
  
C#|   
---|---  
      
    
    public abstract string[] AdditionalFolders {get;}  
  
# Remarks

If absolute path information is not specified, additional folders are created relative to the specification directory.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecialVariables Class](topic4782.md)   
[ProjectSpecialVariables Members](topic4783.md)


