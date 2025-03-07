Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DesignMasterPath Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : DesignMasterPath Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the fully-qualified path to the specification's cached version of the project's design master (see remarks for details). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property DesignMasterPath As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As String
     
    value = instance.DesignMasterPath  
  
C#|   
---|---  
      
    
    public string DesignMasterPath {get;}  
  
# Remarks

For a edit of an existing specification, this is the path to the design master in the existing specification directory. For a new specification, it is the path to the master project's design master.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


